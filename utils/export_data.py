import redis
import json
import os
from datetime import datetime

def export_data():
    """Export all scraped items from Redis to a JSON file."""
    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    
    # Get the total number of items
    item_count = r.llen('spacenets_spider:items')
    if item_count == 0:
        print("No items found in Redis.")
        return
    
    print(f"Found {item_count} items to export.")
    
    # Retrieve all items from the list
    items = []
    batch_size = 100  # Process in batches to handle large datasets
    for start_idx in range(0, item_count, batch_size):
        end_idx = min(start_idx + batch_size - 1, item_count - 1)
        batch_items = r.lrange('spacenets_spider:items', start_idx, end_idx)
        
        for item_json in batch_items:
            try:
                item = json.loads(item_json)
                items.append(item)
            except json.JSONDecodeError as e:
                print(f"Error decoding item: {e}")
    
    # Create export directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"data/spacenets_products_{timestamp}.json"
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully exported {len(items)} items to {filename}")

    # Generate some basic statistics
    categories = {}
    price_min = float('inf')
    price_max = 0
    price_sum = 0
    price_count = 0
    
    for item in items:
        # Count by category
        category = item.get('features', {}).get('Catégorie', 'Unknown')
        categories[category] = categories.get(category, 0) + 1
        
        # Price statistics
        try:
            if item.get('price'):
                price = float(item['price'])
                price_min = min(price_min, price)
                price_max = max(price_max, price)
                price_sum += price
                price_count += 1
        except (ValueError, TypeError):
            pass
    
    # Print statistics
    print("\n--- Data Statistics ---")
    print(f"Total items: {len(items)}")
    print(f"Price range: {price_min:.2f} - {price_max:.2f} TND")
    if price_count > 0:
        print(f"Average price: {price_sum/price_count:.2f} TND")
    
    print("\nTop 5 categories:")
    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {category}: {count} items")

if __name__ == "__main__":
    export_data()