import pandas as pd

class CargoDisruptionOptimizer:
    def __init__(self, flights_df: pd.DataFrame):
        self.flights_df = flights_df

    def evaluate_disruption(self, flight_id: str, delay_minutes: int):
        """
        Evaluates downstream impact of a delayed flight and suggests 
        alternative re-routing options for connecting cargo.
        """
        target_flight = self.flights_df[self.flights_df['flight_id'] == flight_id]
        if target_flight.empty:
            return {"error": "Flight not found"}

        route = target_flight.iloc[0]['route']
        severity = "High" if delay_minutes > 120 else "Moderate"

        recommendations = {
            "flight_id": flight_id,
            "route": route,
            "delay_recorded_mins": delay_minutes,
            "disruption_severity": severity,
            "recommended_action": "Re-book connecting cargo on next available belly-hold capacity" if severity == "High" else "Monitor transit window"
        }
        return recommendations
