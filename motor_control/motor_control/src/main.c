#include <zephyr/kernel.h>
#include <zephyr/net/socket.h>
#include <zephyr/device.h>
#include <zephyr/drivers/pwm.h>
#include <zephyr/sys/printk.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_config.h>
#include <zephyr/data/json.h>
#include <string.h>

#define LED_PWM_NODE DT_ALIAS(pwm_led0)

#if !DT_NODE_HAS_STATUS(LED_PWM_NODE, okay)
#error "Unsupported board: pwm_led0 alias not defined"
#endif

#define PWM_CTLR       DT_PWMS_CTLR(LED_PWM_NODE)
#define PWM_CHANNEL    DT_PWMS_CHANNEL(LED_PWM_NODE)
#define PWM_FLAGS      DT_PWMS_FLAGS(LED_PWM_NODE)
#define PWM_PERIOD_USEC 1000

#define PORT 4242
#define STACK_SIZE 2048
#define THREAD_PRIORITY 5

const struct device *pwm_dev = DEVICE_DT_GET(PWM_CTLR);

void led_server(void)
{
    int server_fd, client_fd;
    struct sockaddr_in addr, client;
    socklen_t client_len = sizeof(client);
    char recv_buf[128];

    server_fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (server_fd < 0) {
        printk("Socket error\n");
        return;
    }

    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(server_fd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        printk("Bind failed\n");
        return;
    }

    if (listen(server_fd, 1) < 0) {
        printk("Listen failed\n");
        return;
    }

    printk("TCP server listening on port %d...\n", PORT);

    while (1) {
        client_fd = accept(server_fd, (struct sockaddr *)&client, &client_len);
        if (client_fd < 0) {
            printk("Accept failed\n");
            continue;
        }

        printk("Client connected\n");

        while (1) {
            int len = recv(client_fd, recv_buf, sizeof(recv_buf) - 1, 0);
            if (len <= 0) {
                printk("Connection closed\n");
                break;
            }

            recv_buf[len] = '\0';
            printk("Received: %s\n", recv_buf);

            struct {
                char command[32];
                int value;
            } cmd;

            const struct json_obj_descr cmd_descr[] = {
                JSON_OBJ_DESCR_PRIM(struct { char command[32]; int value; }, command, JSON_TOK_STRING),
                JSON_OBJ_DESCR_PRIM(struct { char command[32]; int value; }, value, JSON_TOK_NUMBER),
            };

            if (json_obj_parse(recv_buf, len, cmd_descr, ARRAY_SIZE(cmd_descr), &cmd) < 0) {
                printk("Invalid JSON\n");
                continue;
            }

            if (strcmp(cmd.command, "set_brightness") == 0) {
                int brightness = cmd.value;
                if (brightness < 0) brightness = 0;
                if (brightness > 255) brightness = 255;
                uint32_t pulse = (PWM_PERIOD_USEC * brightness) / 255;
                pwm_set(pwm_dev, PWM_CHANNEL, PWM_PERIOD_USEC, pulse, PWM_FLAGS);
                printk("Brightness set to %d\n", brightness);
            } else if (strcmp(cmd.command, "led_on") == 0) {
                pwm_set(pwm_dev, PWM_CHANNEL, PWM_PERIOD_USEC, PWM_PERIOD_USEC, PWM_FLAGS);
                printk("LED turned ON\n");
            } else if (strcmp(cmd.command, "led_off") == 0) {
                pwm_set(pwm_dev, PWM_CHANNEL, PWM_PERIOD_USEC, 0, PWM_FLAGS);
                printk("LED turned OFF\n");
            } else {
                printk("Unknown command: %s\n", cmd.command);
            }
        }

        close(client_fd);
    }
}

K_THREAD_DEFINE(led_server_id, STACK_SIZE, led_server, NULL, NULL, NULL,
                THREAD_PRIORITY, 0, 0);

void main(void)
{
    printk("Zephyr motor_control app with Ethernet + JSON control\n");

    if (!device_is_ready(pwm_dev)) {
        printk("PWM device not ready\n");
        return;
    }
}
