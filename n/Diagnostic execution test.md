#### 4. **Тест выполнения диагностики**

**Метод:** `GET`  
**URL:** `{{baseUrl}}/robots/{{robotId}}/diagnostics`  

**Тесты Postman:**

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Diagnostics data received", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("battery");
    pm.expect(jsonData).to.have.property("motor");
    pm.expect(jsonData).to.have.property("status", "healthy");
});
```