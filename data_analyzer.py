"""
Data Analyzer Module
Analyzes prediction accuracy and provides statistics
"""

import numpy as np
from datetime import datetime, timedelta


class DataAnalyzer:
    """Analyzes prediction data and generates statistics"""
    
    def __init__(self):
        self.predictions_history = []
        self.results_history = []
        
    def add_prediction(self, prediction, result):
        """Add prediction and result to history"""
        self.predictions_history.append(prediction)
        self.results_history.append(result)
    
    def get_statistics(self):
        """Get overall statistics"""
        total = len(self.predictions_history)
        
        if total == 0:
            return {
                'total': 0,
                'accuracy': 0.0,
                'win_rate': 0.0,
                'avg_confidence': 0.0,
                'high_confidence_wins': 0,
                'low_confidence_wins': 0
            }
        
        wins = sum(self.results_history)
        accuracy = wins / total if total > 0 else 0
        
        # Calculate win rate by confidence level
        high_conf = [i for i, p in enumerate(self.predictions_history) if p.get('confidence', 0) > 0.75]
        high_conf_wins = sum(self.results_history[i] for i in high_conf if i < len(self.results_history))
        
        avg_confidence = np.mean([p.get('confidence', 0) for p in self.predictions_history])
        
        return {
            'total': total,
            'accuracy': accuracy,
            'win_rate': wins / total if total > 0 else 0,
            'avg_confidence': avg_confidence,
            'high_confidence_wins': high_conf_wins,
            'low_confidence_wins': wins - high_conf_wins
        }
    
    def get_daily_stats(self):
        """Get statistics for today"""
        today = datetime.now().date()
        today_predictions = [
            (p, r) for p, r in zip(self.predictions_history, self.results_history)
            if datetime.fromisoformat(p.get('timestamp', '')).date() == today
        ]
        
        if not today_predictions:
            return {'date': today, 'total': 0, 'wins': 0, 'accuracy': 0.0}
        
        wins = sum(r for _, r in today_predictions)
        return {
            'date': today,
            'total': len(today_predictions),
            'wins': wins,
            'accuracy': wins / len(today_predictions)
        }
    
    def get_trend_analysis(self, days=7):
        """Analyze trend over specified days"""
        trend_data = []
        
        for i in range(days):
            target_date = (datetime.now() - timedelta(days=i)).date()
            day_predictions = [
                (p, r) for p, r in zip(self.predictions_history, self.results_history)
                if datetime.fromisoformat(p.get('timestamp', '')).date() == target_date
            ]
            
            if day_predictions:
                wins = sum(r for _, r in day_predictions)
                accuracy = wins / len(day_predictions)
                trend_data.append({
                    'date': target_date,
                    'accuracy': accuracy,
                    'total': len(day_predictions)
                })
        
        return trend_data
    
    def get_odds_analysis(self):
        """Analyze odds patterns"""
        if not self.predictions_history:
            return {}
        
        all_odds_high = [p.get('odds', {}).get('high', 1.5) for p in self.predictions_history]
        all_odds_low = [p.get('odds', {}).get('low', 1.5) for p in self.predictions_history]
        
        return {
            'high_odds_mean': np.mean(all_odds_high),
            'high_odds_std': np.std(all_odds_high),
            'low_odds_mean': np.mean(all_odds_low),
            'low_odds_std': np.std(all_odds_low),
            'avg_spread': np.mean([h - l for h, l in zip(all_odds_high, all_odds_low)])
        }
    
    def export_report(self, filename='report.json'):
        """Export analysis report"""
        report = {
            'generated_at': datetime.now().isoformat(),
            'overall_stats': self.get_statistics(),
            'daily_stats': self.get_daily_stats(),
            'trend_analysis': self.get_trend_analysis(),
            'odds_analysis': self.get_odds_analysis()
        }
        
        with open(filename, 'w') as f:
            import json
            json.dump(report, f, indent=2)
        
        return report
