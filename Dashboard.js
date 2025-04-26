import React, { useEffect, useState } from 'react';
import { Bar, Doughnut } from 'react-chartjs-2';

export default function Dashboard() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/metrics')
      .then(res => res.json())
      .then(data => setMetrics(data));
  }, []);

  if (!metrics) return <p>Loading metrics…</p>;

  const report = metrics.classification_report['1'];
  const auc = metrics.auc_roc.toFixed(3);

  const barData = {
    labels: ['Precision', 'Recall', 'F1-Score'],
    datasets: [{
      label: 'Fraud class',
      data: [report.precision, report.recall, report.f1_score],
      backgroundColor: ['rgba(75,192,192,0.6)']
    }]
  };

  const doughnutData = {
    labels: ['Non-Fraud', 'Fraud'],
    datasets: [{
      data: [report.support_total - report.support, report.support],
      backgroundColor: ['#FFCE56', '#FF6384']
    }]
  };

  return (
    <div>
      <h2>Model Performance</h2>
      <p>AUC-ROC: <strong>{auc}</strong></p>
      <div style={{ display: 'flex', gap: '50px' }}>
        <div style={{ width: '300px' }}>
          <Bar data={barData} options={{ responsive: true }} />
        </div>
        <div style={{ width: '300px' }}>
          <Doughnut data={doughnutData} options={{ responsive: true }} />
        </div>
      </div>
    </div>
  );
}
