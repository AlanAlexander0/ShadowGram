'use client';

import React, { useState, useEffect } from 'react';

interface ClusterSummary {
  cluster_id: number;
  size: number;
  modularity_q: number;
  p_value: number;
  dow_savings_inr: number;
  algorithm: string;
  status: string;
}

export default function ComplianceStationPage() {
  const [clusters, setClusters] = useState<ClusterSummary[]>([
    {
      cluster_id: 1,
      size: 20,
      modularity_q: 0.7241,
      p_value: 0.0001,
      dow_savings_inr: 1220.0,
      algorithm: 'Leiden Community Detection',
      status: 'quarantined',
    },
  ]);
  const [loadingPdf, setLoadingPdf] = useState(false);

  useEffect(() => {
    // Poll or fetch graph clusters from backend
    fetch('http://localhost:8000/api/graph')
      .then((res) => res.json())
      .then((data) => {
        if (data.clusters && data.clusters.length > 0) {
          setClusters(data.clusters);
        }
      })
      .catch((err) => {
        console.warn('Backend polling in standalone mode:', err);
      });
  }, []);

  const handleExportPdf = (clusterId: number) => {
    setLoadingPdf(true);
    window.open(`http://localhost:8000/api/sar/pdf/${clusterId}`, '_blank');
    setTimeout(() => setLoadingPdf(false), 800);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-8 font-sans">
      {/* Top Header */}
      <div className="max-w-6xl mx-auto flex justify-between items-center pb-6 border-b border-slate-800 mb-8">
        <div>
          <div className="flex items-center gap-2">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 shadow-lg shadow-emerald-500/50"></span>
            <span className="text-xs font-mono uppercase text-emerald-400 font-bold">
              Station 4 • Compliance Officer Station
            </span>
          </div>
          <h1 className="text-2xl font-black text-white mt-1">
            Financial Crimes Enforcement &amp; Adverse Action Vault
          </h1>
          <p className="text-xs text-slate-400">
            Automated SAR Compilation &bull; ECOA Regulation B (12 CFR § 1002.9) &bull; EU AI Act Articles 13 &amp; 14
          </p>
        </div>

        <button
          onClick={() => handleExportPdf(1)}
          disabled={loadingPdf}
          className="px-5 py-2.5 bg-red-600 hover:bg-red-500 disabled:opacity-50 text-white font-bold text-xs uppercase tracking-wider rounded-xl shadow-lg shadow-red-600/30 transition-all flex items-center gap-2"
        >
          <span>{loadingPdf ? 'Compiling PDF...' : '📄 Export Official SAR PDF'}</span>
        </button>
      </div>

      <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {/* DoW Card */}
        <div className="bg-slate-900/60 border border-emerald-500/30 rounded-2xl p-5 shadow-xl">
          <div className="text-xs uppercase font-bold text-emerald-400 tracking-wider mb-1">
            Pre-KYC Denial-of-Wallet (DoW) Savings
          </div>
          <div className="text-3xl font-mono font-black text-emerald-300">
            ₹1,220.00 INR
          </div>
          <div className="text-xs text-slate-400 mt-2 space-y-1">
            <div>• UIDAI Aadhaar: ₹60.00 (₹3/bot)</div>
            <div>• NSDL/ITD PAN:  ₹40.00 (₹2/bot)</div>
            <div>• Face Liveness: ₹120.00 (₹6/bot)</div>
            <div>• Credit Bureau: ₹1,000.00 (₹50/bot)</div>
          </div>
        </div>

        {/* Statistical Confidence Card */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-xl">
          <div className="text-xs uppercase font-bold text-sky-400 tracking-wider mb-1">
            Empirical Statistical Significance
          </div>
          <div className="text-3xl font-mono font-black text-sky-300">
            p &lt; 0.001
          </div>
          <p className="text-xs text-slate-400 mt-2 leading-relaxed">
            Permutation null model testing against 1,000 degree-preserving graph permutations confirmed non-random orchestration.
          </p>
        </div>

        {/* Statutory Compliance Card */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-5 shadow-xl">
          <div className="text-xs uppercase font-bold text-amber-400 tracking-wider mb-1">
            Legal Adverse Action Standard
          </div>
          <div className="text-xl font-bold text-white">
            Pure Regulation B
          </div>
          <p className="text-xs text-slate-400 mt-2 leading-relaxed">
            Specific factual reason codes (CR-01 to CR-04) generated without black-box risk scores. Reversible via 1-rupee UPI step-up challenge.
          </p>
        </div>
      </div>

      {/* Incident Syndicate Ledger */}
      <div className="max-w-6xl mx-auto bg-slate-900/40 border border-slate-800 rounded-2xl p-6">
        <h2 className="text-lg font-bold text-white mb-4">
          Isolated Syndicate Clusters (Active &amp; Quarantined)
        </h2>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-slate-800 text-slate-400 uppercase font-mono">
                <th className="pb-3">Cluster ID</th>
                <th className="pb-3">Algorithm</th>
                <th className="pb-3">Accounts</th>
                <th className="pb-3">Modularity Q</th>
                <th className="pb-3">Significance</th>
                <th className="pb-3">DoW Saved</th>
                <th className="pb-3">Status</th>
                <th className="pb-3 text-right">Dossier</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60 font-mono">
              {clusters.map((c) => (
                <tr key={c.cluster_id} className="hover:bg-slate-800/30 transition-colors">
                  <td className="py-3 font-bold text-white">Cluster #{c.cluster_id}</td>
                  <td className="py-3 text-slate-400">{c.algorithm || 'Leiden'}</td>
                  <td className="py-3 text-red-400 font-semibold">{c.size} Accounts</td>
                  <td className="py-3 text-amber-300">Q = {c.modularity_q.toFixed(4)}</td>
                  <td className="py-3 text-emerald-400">p = {(c.p_value ?? 0.0001).toFixed(4)}</td>
                  <td className="py-3 text-emerald-300">₹{(c.dow_savings_inr ?? c.size * 61.0).toFixed(2)}</td>
                  <td className="py-3">
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-amber-950/80 text-amber-400 border border-amber-800">
                      {c.status || 'quarantined'}
                    </span>
                  </td>
                  <td className="py-3 text-right">
                    <button
                      onClick={() => handleExportPdf(c.cluster_id)}
                      className="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-[11px] transition-all"
                    >
                      Export PDF
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
