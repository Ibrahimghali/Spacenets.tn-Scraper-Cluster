import redis
import os
import json
import time
import argparse
from datetime import datetime

def connect_to_redis():
    """Connect to Redis using environment variables or defaults."""
    host = os.environ.get('REDIS_HOST', 'localhost')
    port = int(os.environ.get('REDIS_PORT', 6379))
    
    try:
        r = redis.Redis(host=host, port=port, decode_responses=True)
        r.ping()  # Test connection
        return r
    except redis.ConnectionError as e:
        print(f"Error connecting to Redis at {host}:{port}: {e}")
        return None

def get_crawl_stats(r):
    """Get various crawling statistics from Redis."""
    stats = {}
    
    # Pending URLs
    stats['pending_urls'] = r.llen('spacenets:start_urls')
    
    # Dupefilter (visited URLs)
    stats['visited_urls'] = r.scard('spacenets_spider:dupefilter')
    
    # Processed items
    item_keys = r.keys('spacenets_spider:items:*')
    stats['processed_items'] = len(item_keys)
    
    # Queue statistics (requests waiting to be processed)
    queue_keys = r.keys('spacenets_spider:requests*')
    stats['queued_requests'] = sum(r.zcard(key) for key in queue_keys)
    
    # Processing rate (if we have timestamp data)
    stats['processing_rate'] = "N/A"  # Would need additional tracking
    
    # Most recent item
    if item_keys:
        # Get the most recent item key (assuming timestamp in key)
        most_recent_key = sorted(item_keys)[-1]
        item_data = r.get(most_recent_key)
        if item_data:
            try:
                most_recent = json.loads(item_data)
                stats['most_recent_item'] = most_recent.get('name', 'Unknown')
            except json.JSONDecodeError:
                stats['most_recent_item'] = "Error decoding item"
    else:
        stats['most_recent_item'] = "No items yet"
    
    return stats

def print_stats(stats):
    """Pretty print the crawling statistics."""
    print("\n" + "="*60)
    print(f"SPACENETS CRAWLING PROGRESS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    print(f"🔄 Pending Start URLs: {stats['pending_urls']}")
    print(f"👁️ Visited URLs: {stats['visited_urls']}")
    print(f"📦 Processed Items: {stats['processed_items']}")
    print(f"⏳ Queued Requests: {stats['queued_requests']}")
    print(f"⚡ Processing Rate: {stats['processing_rate']}")
    print(f"🆕 Most Recent Item: {stats['most_recent_item']}")
    
    print("="*60 + "\n")

def sample_items(r, count=3):
    """Show a sample of collected items."""
    item_keys = r.keys('spacenets_spider:items:*')
    
    if not item_keys:
        print("No items collected yet.")
        return
    
    sample_size = min(count, len(item_keys))
    sampled_keys = sorted(item_keys, reverse=True)[:sample_size]
    
    print(f"\nSAMPLE OF {sample_size} RECENT ITEMS:")
    print("-"*60)
    
    for key in sampled_keys:
        try:
            item_data = r.get(key)
            if item_data:
                item = json.loads(item_data)
                print(f"Item: {item.get('name', 'Unknown')}")
                print(f"Price: {item.get('formatted_price', 'N/A')}")
                print("-"*30)
        except json.JSONDecodeError:
            print(f"Error decoding item with key: {key}")
    
    print("")

def main():
    parser = argparse.ArgumentParser(description='Monitor Redis-based scraping progress')
    parser.add_argument('--continuous', '-c', action='store_true', 
                        help='Continuously monitor (updates every 5 seconds)')
    parser.add_argument('--sample', '-s', type=int, default=0,
                        help='Show sample of N most recent items')
    
    args = parser.parse_args()
    
    r = connect_to_redis()
    if not r:
        return
    
    if args.continuous:
        try:
            while True:
                stats = get_crawl_stats(r)
                print_stats(stats)
                if args.sample > 0:
                    sample_items(r, args.sample)
                time.sleep(5)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
    else:
        stats = get_crawl_stats(r)
        print_stats(stats)
        if args.sample > 0:
            sample_items(r, args.sample)

if __name__ == "__main__":
    main()