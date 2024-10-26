#### 2. **Тест создания расписания**

**Метод:** `POST`  
**URL:** `{{baseUrl}}/robots/{{robotId}}/schedule`  
**Тело запроса:**

```json
{
  "room": "Living Room",
  "time": "08:00 AM"
}
```

**Тесты Postman:**

```javascript
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Schedule created successfully", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("room", "Living Room");
    pm.expect(jsonData).to.have.property("time", "08:00 AM");
});
```