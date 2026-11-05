const { test, expect } = require('@playwright/test');

test('home page shows the lab heading', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle('Lab App');
  await expect(page.getByRole('heading', { name: 'Test Automation Lab' })).toBeVisible();
});
