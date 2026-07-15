"""
Betika Aviator Scraper Module
Scrapes real-time Aviator data from Betika.com
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import json
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BetikaAviatorScraper:
    """Scrapes Aviator game data from Betika.com"""
    
    def __init__(self):
        self.base_url = "https://www.betika.com/en-ke/games/aviator"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.session = requests.Session()
        self.driver = None
        self.recent_results = []
        
    def scrape_with_requests(self):
        """Scrape public data using requests library"""
        try:
            logger.info("Scraping Betika Aviator with requests...")
            response = self.session.get(self.base_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Try to find recent results
            results = self._parse_results(soup)
            logger.info(f"Found {len(results)} recent results")
            
            return results
            
        except Exception as e:
            logger.error(f"Error scraping with requests: {e}")
            return []
    
    def scrape_with_selenium(self):
        """Scrape dynamic data using Selenium browser automation"""
        try:
            logger.info("Scraping Betika Aviator with Selenium...")
            
            # Initialize Chrome driver
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            self.driver = webdriver.Chrome(options=options)
            self.driver.get(self.base_url)
            
            # Wait for dynamic content to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "crash-result"))
            )
            
            # Extract recent crash values
            crash_elements = self.driver.find_elements(By.CLASS_NAME, "crash-result")
            results = []
            
            for element in crash_elements[:20]:  # Get last 20 results
                try:
                    crash_value = element.text
                    results.append({
                        'value': float(crash_value.replace('x', '').strip()),
                        'timestamp': datetime.now().isoformat(),
                        'source': 'betika_selenium'
                    })
                except:
                    continue
            
            logger.info(f"Scraped {len(results)} results with Selenium")
            self.recent_results = results
            return results
            
        except Exception as e:
            logger.error(f"Error scraping with Selenium: {e}")
            return []
        finally:
            if self.driver:
                self.driver.quit()
    
    def _parse_results(self, soup):
        """Parse HTML soup to extract results"""
        results = []
        
        # Look for common result container patterns
        # Note: These selectors may need adjustment based on actual Betika HTML
        result_containers = soup.find_all('div', class_=['result', 'crash-history', 'recent-result'])
        
        for container in result_containers:
            try:
                # Try different ways to extract the value
                value_text = container.get_text(strip=True)
                
                # Extract numeric value (e.g., "1.45x")
                import re
                match = re.search(r'(\d+\.\d+)x?', value_text)
                
                if match:
                    crash_value = float(match.group(1))
                    results.append({
                        'value': crash_value,
                        'timestamp': datetime.now().isoformat(),
                        'source': 'betika_requests'
                    })
            except Exception as e:
                logger.debug(f"Error parsing result: {e}")
                continue
        
        return results
    
    def get_live_data(self):
        """Get current live game data"""
        try:
            data = self.scrape_with_requests()
            
            if not data:
                logger.info("Requests scraping failed, trying Selenium...")
                data = self.scrape_with_selenium()
            
            if data:
                # Calculate statistics
                values = [d['value'] for d in data]
                return {
                    'recent_results': data,
                    'average': sum(values) / len(values),
                    'high': max(values),
                    'low': min(values),
                    'count': len(values),
                    'last_updated': datetime.now().isoformat()
                }
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting live data: {e}")
            return None
    
    def predict_next_crash(self, history_data):
        """Predict next crash value based on history"""
        if not history_data or len(history_data) < 10:
            return None
        
        values = [d['value'] for d in history_data[-50:]]  # Last 50
        
        # Calculate trend
        avg = sum(values) / len(values)
        std_dev = (sum((x - avg) ** 2 for x in values) / len(values)) ** 0.5
        
        # Simple prediction based on statistics
        prediction = {
            'predicted_value': avg,
            'confidence': 0.5 + (std_dev / avg) * 0.3,  # Confidence based on volatility
            'range_low': avg - std_dev,
            'range_high': avg + std_dev,
            'timestamp': datetime.now().isoformat()
        }
        
        return prediction
    
    def export_data(self, filename='betika_results.json'):
        """Export scraped data to JSON"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.recent_results, f, indent=2)
            logger.info(f"Data exported to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error exporting data: {e}")
            return False


# Alternative: Using API intercepting (Advanced)
class BetikaAPIInterceptor:
    """Intercepts Betika API calls using browser automation"""
    
    def __init__(self):
        self.base_url = "https://www.betika.com"
        self.api_calls = []
        
    def setup_mitmproxy(self):
        """Setup MITM proxy to intercept requests"""
        logger.info("Setting up MITM proxy for API interception...")
        # This requires mitmproxy to be installed and configured
        # Advanced users only
        pass
    
    def get_intercepted_apis(self):
        """Get APIs intercepted from network traffic"""
        return self.api_calls


# Standalone function for quick scraping
def quick_scrape_betika():
    """Quick function to scrape Betika Aviator data"""
    scraper = BetikaAviatorScraper()
    
    logger.info("Starting quick Betika Aviator scrape...")
    
    # Try requests first (faster)
    data = scraper.get_live_data()
    
    if data:
        logger.info(f"✓ Successfully scraped Betika data:")
        logger.info(f"  - Recent results: {len(data['recent_results'])}")
        logger.info(f"  - Average crash: {data['average']:.2f}x")
        logger.info(f"  - High: {data['high']:.2f}x, Low: {data['low']:.2f}x")
        
        # Make prediction
        prediction = scraper.predict_next_crash(data['recent_results'])
        if prediction:
            logger.info(f"✓ Prediction: {prediction['predicted_value']:.2f}x (Confidence: {prediction['confidence']:.2%})")
        
        return data
    else:
        logger.error("✗ Failed to scrape Betika data")
        return None


if __name__ == '__main__':
    # Test the scraper
    result = quick_scrape_betika()
    if result:
        print(json.dumps(result, indent=2))
