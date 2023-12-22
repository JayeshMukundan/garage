package com.sj.urlshortener.pubsub;
import com.sj.urlshortener.model.UrlUsage;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;

@Component
public class UrlUsagePublisher {

    private final RedisTemplate<String, Object> redisTemplate;

    public UrlUsagePublisher(RedisTemplate<String, Object> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    public void publishMessage(UrlUsage urlUsage) {
        redisTemplate.convertAndSend(Channel.URL_USAGE, urlUsage);
    }
}
