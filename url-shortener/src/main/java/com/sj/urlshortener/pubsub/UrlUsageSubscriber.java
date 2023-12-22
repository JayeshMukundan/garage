package com.sj.urlshortener.pubsub;

import com.sj.urlshortener.controller.UrlShortenerController;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.redis.connection.Message;
import org.springframework.data.redis.connection.MessageListener;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import java.nio.charset.StandardCharsets;


@Component
public class UrlUsageSubscriber implements MessageListener {

    private RedisTemplate<String, Object> redisTemplate;

    private static final Logger log = LoggerFactory.getLogger(UrlUsageSubscriber.class);

    public UrlUsageSubscriber(RedisTemplate<String, Object> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    @Transactional
    public void onMessage(Message message) {
        Object messagePayload = redisTemplate.getValueSerializer().deserialize(message.getBody());
        // Process the received message here
        log.info("Received message = {}", messagePayload);

        // Acknowledge the message
    }

    @Override
    @Transactional
    public void onMessage(Message message, byte[] pattern) {
        Object messagePayload = redisTemplate.getValueSerializer().deserialize(message.getBody());
        // Process the received message here
        log.info("Received message2 = {}, pattern = {}", messagePayload,  new String(pattern));

        // Acknowledge the message

    }
}
