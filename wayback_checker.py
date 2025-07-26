#!/usr/bin/env python3
"""
Wayback Machine Timestamp Verification Tool
Based on the temporal forensics investigation plan
"""

import requests
import json
import sys
from datetime import datetime
import argparse

def check_wayback_machine(url):
    """
    Query the Wayback Machine for snapshot history of a URL
    """
    wayback_api = 'http://web.archive.org/__wb/sparkline'
    params = {
        'url': url,
        'collection': 'web',
        'output': 'json'
    }
    
    try:
        print(f"Querying Wayback Machine for: {url}")
        response = requests.get(wayback_api, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if 'first_ts' in data and data['first_ts']:
            first_snapshot = data['first_ts']
            # Convert timestamp format (YYYYMMDDHHMMSS) to readable date
            if len(str(first_snapshot)) >= 8:
                date_str = str(first_snapshot)[:8]
                formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
                print(f"✓ First snapshot found: {formatted_date}")
                print(f"  Raw timestamp: {first_snapshot}")
                
                # Check if there are multiple snapshots
                if 'last_ts' in data and data['last_ts']:
                    last_snapshot = data['last_ts']
                    last_date_str = str(last_snapshot)[:8]
                    last_formatted = f"{last_date_str[:4]}-{last_date_str[4:6]}-{last_date_str[6:8]}"
                    print(f"  Last snapshot: {last_formatted}")
                    print(f"  Total snapshots: {data.get('count', 'Unknown')}")
                
                return {
                    'found': True,
                    'first_snapshot': first_snapshot,
                    'first_date': formatted_date,
                    'data': data
                }
            else:
                print("⚠ Invalid timestamp format received")
                return {'found': False, 'error': 'Invalid timestamp format'}
        else:
            print("✗ No snapshots found in Wayback Machine")
            return {'found': False, 'error': 'No snapshots found'}
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Error querying Wayback Machine: {e}")
        return {'found': False, 'error': str(e)}
    except json.JSONDecodeError as e:
        print(f"✗ Error parsing response: {e}")
        return {'found': False, 'error': f'JSON decode error: {e}'}

def check_specific_snapshot(url, date=None):
    """
    Check if a specific snapshot exists for a given date
    """
    if date:
        # Format: YYYYMMDD or YYYYMMDDHHMMSS
        wayback_url = f"http://archive.org/wayback/available?url={url}&timestamp={date}"
    else:
        wayback_url = f"http://archive.org/wayback/available?url={url}"
    
    try:
        response = requests.get(wayback_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('archived_snapshots', {}).get('closest'):
            snapshot = data['archived_snapshots']['closest']
            print(f"✓ Closest snapshot found:")
            print(f"  Date: {snapshot.get('timestamp', 'Unknown')}")
            print(f"  URL: {snapshot.get('url', 'Unknown')}")
            print(f"  Status: {snapshot.get('status', 'Unknown')}")
            return snapshot
        else:
            print("✗ No archived snapshots found")
            return None
            
    except Exception as e:
        print(f"✗ Error checking specific snapshot: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Check Wayback Machine for URL snapshots')
    parser.add_argument('url', help='URL to check in Wayback Machine')
    parser.add_argument('--date', help='Specific date to check (YYYYMMDD format)', default=None)
    parser.add_argument('--output', help='Output file for results', default=None)
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("WAYBACK MACHINE TIMESTAMP VERIFICATION")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("=" * 60)
    
    results = {
        'url': args.url,
        'analysis_date': datetime.now().isoformat(),
        'sparkline_check': None,
        'specific_snapshot': None
    }
    
    # Check general snapshot history
    print("\n1. CHECKING SNAPSHOT HISTORY...")
    sparkline_result = check_wayback_machine(args.url)
    results['sparkline_check'] = sparkline_result
    
    # Check specific snapshot if date provided
    if args.date:
        print(f"\n2. CHECKING SPECIFIC DATE: {args.date}")
        snapshot_result = check_specific_snapshot(args.url, args.date)
        results['specific_snapshot'] = snapshot_result
    else:
        print("\n2. CHECKING LATEST AVAILABLE SNAPSHOT...")
        snapshot_result = check_specific_snapshot(args.url)
        results['specific_snapshot'] = snapshot_result
    
    # Save results if output file specified
    if args.output:
        try:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            print(f"\n✓ Results saved to: {args.output}")
        except Exception as e:
            print(f"\n✗ Error saving results: {e}")
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    
    # Return appropriate exit code
    if sparkline_result.get('found') or results['specific_snapshot']:
        return 0  # Found snapshots
    else:
        return 1  # No snapshots found

if __name__ == "__main__":
    sys.exit(main()) 