Examples
========

This section provides comprehensive examples of using the Polish Energy Regulatory Office library
for various real-world scenarios.

.. toctree::
   :maxdepth: 2

   basic_usage
   advanced_analysis
   data_visualization
   automated_reporting
   integration_examples

Basic Usage Examples
--------------------

Simple Price Analysis
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
   from datetime import date, timedelta

   # Analyze last 30 days of price data
   analyzer = EnergyPriceAnalyzer()
   end_date = date.today()
   start_date = end_date - timedelta(days=30)

   trends = analyzer.analyze_price_trends(start_date, end_date)

   print(f"Average price: {trends.average_price:.2f} PLN/MWh")
   print(f"Price volatility: {trends.volatility:.2f}%")
   print(f"Trend direction: {trends.trend_direction}")

Finding Renewable Installations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.renewable_energy_sources_mapper import RenewableMapper

   mapper = RenewableMapper()

   # Find all solar installations above 1 MW
   solar_installations = mapper.filter_installations(
       technology="solar",
       min_capacity_mw=1.0
   )

   total_capacity = sum(inst.capacity_mw for inst in solar_installations)
   print(f"Total solar capacity above 1 MW: {total_capacity:.1f} MW")

Advanced Analysis Examples
--------------------------

Comparative Regional Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.renewable_energy_sources_mapper import RenewableMapper
   import pandas as pd

   mapper = RenewableMapper()
   regions = ["mazowieckie", "śląskie", "wielkopolskie", "małopolskie"]

   regional_data = []
   for region in regions:
       installations = mapper.get_installations_by_region(region)
       total_capacity = sum(inst.capacity_mw for inst in installations)
       regional_data.append({
           "region": region,
           "installations_count": len(installations),
           "total_capacity_mw": total_capacity,
           "average_size_mw": total_capacity / len(installations) if installations else 0
       })

   df = pd.DataFrame(regional_data)
   print(df)

Price Correlation Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
   import matplotlib.pyplot as plt
   import pandas as pd

   analyzer = EnergyPriceAnalyzer()

   # Get price data for different market segments
   day_ahead_prices = analyzer.get_price_data("day_ahead", start_date, end_date)
   intraday_prices = analyzer.get_price_data("intraday", start_date, end_date)

   # Create correlation analysis
   df = pd.DataFrame({
       'day_ahead': [p.price_pln_mwh for p in day_ahead_prices],
       'intraday': [p.price_pln_mwh for p in intraday_prices]
   })

   correlation = df.corr()
   print(f"Price correlation: {correlation.iloc[0, 1]:.3f}")

Data Visualization Examples
---------------------------

Installation Growth Over Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.microinstallation_mapper import MicroinstallationMapper
   import matplotlib.pyplot as plt
   import pandas as pd
   from datetime import date, timedelta

   mapper = MicroinstallationMapper()

   # Get monthly installation data for the past year
   monthly_data = []
   for i in range(12):
       month_start = date.today().replace(day=1) - timedelta(days=30*i)
       month_end = month_start.replace(day=28) + timedelta(days=4)

       installations = mapper.get_installations_by_period(month_start, month_end)
       monthly_data.append({
           'month': month_start.strftime('%Y-%m'),
           'count': len(installations),
           'capacity_kw': sum(inst.capacity_kw for inst in installations)
       })

   df = pd.DataFrame(monthly_data)

   # Create visualization
   fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

   ax1.plot(df['month'], df['count'], marker='o')
   ax1.set_title('Monthly Microinstallation Count')
   ax1.set_ylabel('Number of Installations')

   ax2.plot(df['month'], df['capacity_kw'], marker='s', color='orange')
   ax2.set_title('Monthly Installed Capacity')
   ax2.set_ylabel('Capacity (kW)')

   plt.tight_layout()
   plt.show()

Regional Distribution Map
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.renewable_energy_sources_mapper import RenewableMapper
   import folium

   mapper = RenewableMapper()
   installations = mapper.get_all_installations()

   # Create map centered on Poland
   m = folium.Map(location=[52.0, 19.0], zoom_start=6)

   for installation in installations:
       if installation.latitude and installation.longitude:
           folium.CircleMarker(
               location=[installation.latitude, installation.longitude],
               radius=max(3, installation.capacity_mw / 10),
               popup=f"{installation.name}: {installation.capacity_mw} MW",
               color='red' if installation.technology == 'wind' else 'blue',
               fill=True
           ).add_to(m)

   m.save('renewable_installations_map.html')

Automated Reporting Examples
----------------------------

Daily Price Report
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
   from datetime import date
   import smtplib
   from email.mime.text import MIMEText

   def generate_daily_price_report():
       analyzer = EnergyPriceAnalyzer()
       today = date.today()

       # Get today's price data
       prices = analyzer.get_daily_prices(today)
       avg_price = sum(p.price_pln_mwh for p in prices) / len(prices)

       # Compare with yesterday
       yesterday_prices = analyzer.get_daily_prices(today - timedelta(days=1))
       yesterday_avg = sum(p.price_pln_mwh for p in yesterday_prices) / len(yesterday_prices)

       change = ((avg_price - yesterday_avg) / yesterday_avg) * 100

       report = f"""
       Daily Energy Price Report - {today}

       Average Price Today: {avg_price:.2f} PLN/MWh
       Average Price Yesterday: {yesterday_avg:.2f} PLN/MWh
       Change: {change:+.2f}%

       Price Range: {min(p.price_pln_mwh for p in prices):.2f} - {max(p.price_pln_mwh for p in prices):.2f} PLN/MWh
       """

       return report

   # Generate and send report
   report = generate_daily_price_report()
   print(report)

Weekly Audit Summary
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from polish_energy_regulatory_office.energy_efficiency_audit_tool import EnergyAuditor
   from datetime import date, timedelta

   def generate_weekly_audit_summary():
       auditor = EnergyAuditor()
       end_date = date.today()
       start_date = end_date - timedelta(days=7)

       audits = auditor.get_audits_by_period(start_date, end_date)

       summary = {
           'total_audits': len(audits),
           'avg_efficiency_score': sum(a.efficiency_score for a in audits) / len(audits),
           'compliance_rate': len([a for a in audits if a.is_compliant]) / len(audits) * 100,
           'recommendations_issued': sum(len(a.recommendations) for a in audits)
       }

       return summary

Integration Examples
--------------------

Flask Web Application
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from flask import Flask, jsonify, request
   from polish_energy_regulatory_office.energy_price_analyzer import EnergyPriceAnalyzer
   from datetime import date, datetime

   app = Flask(__name__)
   analyzer = EnergyPriceAnalyzer()

   @app.route('/api/prices/current')
   def get_current_prices():
       today = date.today()
       prices = analyzer.get_daily_prices(today)
       return jsonify([{
           'timestamp': p.timestamp.isoformat(),
           'price_pln_mwh': p.price_pln_mwh,
           'market_segment': p.market_segment
       } for p in prices])

   @app.route('/api/trends')
   def get_price_trends():
       start_date = datetime.strptime(request.args.get('start'), '%Y-%m-%d').date()
       end_date = datetime.strptime(request.args.get('end'), '%Y-%m-%d').date()

       trends = analyzer.analyze_price_trends(start_date, end_date)
       return jsonify({
           'average_price': trends.average_price,
           'volatility': trends.volatility,
           'trend_direction': trends.trend_direction
       })

   if __name__ == '__main__':
       app.run(debug=True)

Celery Background Tasks
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from celery import Celery
   from polish_energy_regulatory_office.renewable_energy_sources_mapper import RenewableMapper
   from polish_energy_regulatory_office.microinstallation_mapper import MicroinstallationMapper

   app = Celery('pero_tasks', broker='redis://localhost:6379')

   @app.task
   def update_renewable_installations():
       mapper = RenewableMapper()
       new_installations = mapper.fetch_latest_installations()
       mapper.save_to_database(new_installations)
       return f"Updated {len(new_installations)} installations"

   @app.task
   def process_microinstallation_applications():
       mapper = MicroinstallationMapper()
       pending_applications = mapper.get_pending_applications()

       processed = 0
       for application in pending_applications:
           result = mapper.process_application(application)
           if result.success:
               processed += 1

       return f"Processed {processed} applications"

   # Schedule tasks
   from celery.schedules import crontab

   app.conf.beat_schedule = {
       'update-installations-daily': {
           'task': 'update_renewable_installations',
           'schedule': crontab(hour=6, minute=0),
       },
       'process-applications-hourly': {
           'task': 'process_microinstallation_applications',
           'schedule': crontab(minute=0),
       },
   }
