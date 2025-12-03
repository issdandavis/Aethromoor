/**
 * Polly's Wingscroll - Analytics and Event Tracing Module
 * 
 * @fileoverview Lightweight tracing for user journey, statistics, and game events
 * @version 1.0.0
 * @copyright (c) 2024 Polly's Wingscroll Project
 * @license All Rights Reserved
 * 
 * This module captures player choices, stat evolution, and endings for:
 * - Analytics and player behavior analysis
 * - Game balance optimization
 * - Bug tracking and debugging
 * - AI agent review and improvement
 * 
 * Privacy Note: All data is stored locally in browser memory only.
 * No data is transmitted to external servers unless explicitly configured.
 */

(function(){
  'use strict';
  
  /**
   * Main trace object containing all session data
   * @type {Object}
   */
  const trace = {
    sessionId: Date.now().toString(36) + '-' + Math.random().toString(16).slice(2),
    startedAt: new Date().toISOString(),
    events: [],
    version: '1.0.0'
  };

  /**
   * Record a game event with timestamp
   * @param {string} type - Event type (e.g., 'choice_made', 'ending_reached')
   * @param {Object} payload - Additional event data
   */
  function traceEvent(type, payload = {}) {
    try {
      trace.events.push({
        t: new Date().toISOString(),
        type,
        ...payload
      });
      
      // Optional: Send to analytics service (if configured)
      if (window.GAME_CONFIG && window.GAME_CONFIG.enableAnalytics) {
        sendToAnalytics(type, payload);
      }
    } catch (error) {
      console.error('Trace event error:', error);
    }
  }

  /**
   * Export trace data as JSON string
   * @returns {string} Formatted JSON of all trace data
   */
  function exportTrace() {
    return JSON.stringify(trace, null, 2);
  }

  /**
   * Download trace data as a file
   * Useful for user feedback and bug reports
   */
  function downloadTrace() {
    try {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(exportTrace());
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `polly-wingscroll-trace-${trace.sessionId}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    } catch (error) {
      console.error('Failed to download trace:', error);
    }
  }

  /**
   * Clear all trace events (keeps session ID)
   */
  function clearTrace() {
    trace.events.length = 0;
    trace.startedAt = new Date().toISOString();
    traceEvent('trace_reset', {});
  }

  /**
   * Get statistics summary from trace data
   * @returns {Object} Summary statistics
   */
  function getTraceSummary() {
    return {
      sessionId: trace.sessionId,
      duration: new Date() - new Date(trace.startedAt),
      eventCount: trace.events.length,
      choicesMade: trace.events.filter(e => e.type === 'choice_made').length,
      errors: trace.events.filter(e => e.type === 'error').length
    };
  }

  /**
   * Placeholder for analytics service integration
   * @param {string} type - Event type
   * @param {Object} payload - Event data
   */
  function sendToAnalytics(type, payload) {
    // TODO: Implement analytics service integration
    // Example: Google Analytics, Mixpanel, or custom backend
    console.log('[Analytics]', type, payload);
  }

  // Expose public API
  window.gameTrace = trace;
  window.traceEvent = traceEvent;
  window.exportTrace = exportTrace;
  window.downloadTrace = downloadTrace;
  window.clearTrace = clearTrace;
  window.getTraceSummary = getTraceSummary;
  
  // Log initialization
  console.log('Game trace initialized:', trace.sessionId);
})();
