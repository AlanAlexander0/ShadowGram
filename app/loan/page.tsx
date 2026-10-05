/**
 * app/loan/page.tsx - AthenaPay Target Micro-Lending Portal (Laptop 3)
 * Assignee: Alan E Alexander (Role 3: Red-Team Swarm Runner & Client Telemetry Lead)
 * Document Code: SG-PROTO-00 / Task 3.4
 * 
 * The 6-Second Judge Testing Rule:
 * - 95% of inputs are pre-filled (Name, PAN, Income, Amount).
 * - ONLY 1 blank field: "Loan Reason [ Type 3 words ]".
 * - High-contrast glowing button: [ >> APPLY NOW << ].
 * - Silently instrumented by /telemetry.js for zero-PII physical telemetry capture.
 */

'use client';

import React, { useState, useEffect } from 'react';
import Script from 'next/script';

export default function AthenaPayLoanPage() {
  const [loanReason, setLoanReason] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [approvedAmount, setApprovedAmount] = useState<number | null>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!loanReason.trim()) return;

    // Send final submission trigger to telemetry SDK if available
    if (typeof window !== 'undefined' && (window as any).ShadowGramTelemetry) {
      (window as any).ShadowGramTelemetry.pushEvent('pointerdown', {
        route_path: '/loan -> /loan_approved',
        reason_length: loanReason.length,
        is_live_judge: true
      });
      (window as any).ShadowGramTelemetry.flush();
    }

    setApprovedAmount(10000);
    setSubmitted(true);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col items-center justify-center p-4 antialiased selection:bg-cyan-500 selection:text-black">
      {/* Telemetry SDK Hook (Zero-PII, 50ms Throttled, HMAC-signed) */}
      <Script src="/telemetry.js" strategy="afterInteractive" />

      <div className="w-full max-w-md bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-2xl backdrop-blur-xl relative overflow-hidden">
        {/* Ambient Top Glow */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-1 bg-gradient-to-r from-transparent via-cyan-500 to-transparent" />

        {/* Brand Header */}
        <div className="flex items-center justify-between mb-6 pb-4 border-b border-slate-800/80">
          <div>
            <div className="flex items-center gap-2">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse" />
              <h1 className="text-xl font-bold tracking-tight text-white">AthenaPay Instant Credit</h1>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">Station 3: Live Judge Evaluation Terminal</p>
          </div>
          <span className="text-[10px] font-mono uppercase px-2 py-1 rounded bg-cyan-950/80 text-cyan-400 border border-cyan-800">
            6s Test Ready
          </span>
        </div>

        {!submitted ? (
          <form onSubmit={handleSubmit} className="space-y-4">
            {/* Pre-populated inputs (95% complete) */}
            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-medium text-slate-400 mb-1">Applicant Name</label>
                <input
                  id="input-name"
                  type="text"
                  readOnly
                  defaultValue="Rohan Verma"
                  className="w-full bg-slate-800/60 border border-slate-700/60 rounded-lg px-3 py-2 text-sm text-slate-300 cursor-not-allowed select-none"
                />
              </div>
              <div>
                <label className="block text-xs font-medium text-slate-400 mb-1">PAN Identification</label>
                <input
                  id="input-pan"
                  type="text"
                  readOnly
                  defaultValue="ABCDE1234F"
                  className="w-full bg-slate-800/60 border border-slate-700/60 rounded-lg px-3 py-2 text-sm font-mono text-slate-300 cursor-not-allowed select-none"
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-medium text-slate-400 mb-1">Verified Income</label>
                <input
                  type="text"
                  readOnly
                  defaultValue="INR 45,000 / mo"
                  className="w-full bg-slate-800/60 border border-slate-700/60 rounded-lg px-3 py-2 text-sm text-slate-300 cursor-not-allowed select-none"
                />
              </div>
              <div>
                <label className="block text-xs font-medium text-slate-400 mb-1">Pre-Approved Limit</label>
                <input
                  id="input-amount"
                  type="text"
                  readOnly
                  defaultValue="INR 10,000"
                  className="w-full bg-slate-800/60 border border-slate-700/60 rounded-lg px-3 py-2 text-sm font-semibold text-emerald-400 cursor-not-allowed select-none"
                />
              </div>
            </div>

            {/* Honey-DOM Tripwire (Hidden from human visual viewport, traps dumb bots) */}
            <div
              id="honey-dom-profile-sync"
              data-honey="tripwire"
              aria-hidden="true"
              style={{ position: 'absolute', opacity: 0, pointerEvents: 'none', height: 0, width: 0, zIndex: -1 }}
            >
              <input type="text" name="bot_honey_sync" tabIndex={-1} defaultValue="" />
            </div>

            {/* The ONLY editable field for the Judge */}
            <div className="pt-2">
              <label className="block text-xs font-semibold text-cyan-400 mb-1.5 flex items-center justify-between">
                <span>Loan Purpose (Type 3 words):</span>
                <span className="text-[11px] font-normal text-slate-400 font-mono">e.g. Laptop repair fee</span>
              </label>
              <input
                id="input-reason"
                type="text"
                autoFocus
                required
                placeholder="Type 3 words here..."
                value={loanReason}
                onChange={(e) => setLoanReason(e.target.value)}
                className="w-full bg-slate-800 border-2 border-cyan-500/80 focus:border-cyan-400 focus:ring-4 focus:ring-cyan-500/20 rounded-lg px-3.5 py-2.5 text-white placeholder-slate-500 text-sm font-medium outline-none transition-all shadow-inner"
              />
            </div>

            {/* High-Contrast Glowing Action Button */}
            <button
              id="btn-apply"
              type="submit"
              className="w-full mt-4 py-3 px-4 rounded-xl font-bold text-sm tracking-wider uppercase bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-black shadow-lg shadow-cyan-500/30 hover:shadow-cyan-400/50 hover:scale-[1.01] active:scale-[0.99] transition-all duration-150 flex items-center justify-center gap-2 cursor-pointer"
            >
              <span>&gt;&gt; APPLY NOW (INSTANT DISBURSAL) &lt;&lt;</span>
            </button>
          </form>
        ) : (
          <div className="text-center py-8 space-y-4">
            <div className="w-16 h-16 rounded-full bg-emerald-500/20 border-2 border-emerald-400 text-emerald-400 flex items-center justify-center mx-auto text-2xl animate-bounce">
              ✓
            </div>
            <div>
              <h2 className="text-lg font-bold text-white">Application Approved!</h2>
              <p className="text-sm text-slate-400 mt-1">
                Disbursing <span className="text-emerald-400 font-semibold font-mono">INR {approvedAmount?.toLocaleString()}</span> to linked account.
              </p>
            </div>
            <div className="p-3 rounded-lg bg-slate-800/80 border border-slate-700 text-xs text-left font-mono space-y-1 text-slate-300">
              <div className="flex justify-between">
                <span className="text-slate-500">Applicant:</span>
                <span>Rohan Verma</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Classification:</span>
                <span className="text-emerald-400 font-bold">ORGANIC_HUMAN (Passed Layer 1-5)</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Telemetry Stream:</span>
                <span className="text-cyan-400">Captured & Verified</span>
              </div>
            </div>
            <button
              onClick={() => {
                setSubmitted(false);
                setLoanReason('');
              }}
              className="text-xs text-slate-400 hover:text-white underline transition-colors cursor-pointer"
            >
              Reset for Next Judge
            </button>
          </div>
        )}

        <div className="mt-5 pt-3 border-t border-slate-800 text-[11px] text-slate-500 flex justify-between items-center">
          <span>Protected by ShadowGram Relational Forensics</span>
          <span className="font-mono">v2.0-HackAthena</span>
        </div>
      </div>
    </div>
  );
}
