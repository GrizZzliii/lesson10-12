#### 3. **Тест обновления статуса робота**

**Метод:** `PUT`  
**URL:** `{{baseUrl}}/robots/{{robotId}}/status`  
**Тело запроса:**

```json
{
  "status": "active"
}
```

**Тесты Postman:**

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Status updated successfully", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("status", "active");
});
```
