import os

def try_parse_int(value: str):
    try:
        return int(value)
    except Exception:
        return None

def get_store_api_base_url():
    host = os.environ.get("STORE_API_HOST") or "localhost"
    port = try_parse_int(os.environ.get("STORE_API_PORT")) or 8000
    return f"http://{host}:{port}"

def get_redis_config():
    host = os.environ.get("REDIS_HOST") or "localhost"
    port = try_parse_int(os.environ.get("REDIS_PORT")) or 6379
    return host, port

def get_hub_logic_config():
    batch_size = try_parse_int(os.environ.get("BATCH_SIZE")) or 20
    return batch_size

def get_mqtt_config():
    broker_host = os.environ.get("MQTT_BROKER_HOST") or "localhost"
    broker_port = try_parse_int(os.environ.get("MQTT_BROKER_PORT")) or 1883
    topic = os.environ.get("MQTT_TOPIC") or "processed_agent_data_topic"
    return broker_host, broker_port, topic

# Usage examples
store_api_url = get_store_api_base_url()
redis_host, redis_port = get_redis_config()
batch_size = get_hub_logic_config()
mqtt_broker_host, mqtt_broker_port, mqtt_topic = get_mqtt_config()
