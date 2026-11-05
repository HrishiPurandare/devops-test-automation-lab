const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: 'tests',
  use: { baseURL: process.env.APP_URL || 'http://app:5000' },
  reporter: [['list'], ['html', { outputFolder: '/reports/ui', open: 'never' }]],
  outputDir: '/tmp/test-results',
});
