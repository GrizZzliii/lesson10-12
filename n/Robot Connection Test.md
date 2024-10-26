#### 1. **Тест подключения робота**

**Метод:** `POST`  
**URL:** `{{baseUrl}}/robots`  
**Тело запроса:**

```json
{
  "name": "Robot-1",
  "model": "X1000"
}
```

**Тесты Postman:**

```javascript
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Robot ID is returned", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("id");
    pm.environment.set("robotId", jsonData.id);
});
```
