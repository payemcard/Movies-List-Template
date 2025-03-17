# Movie Website Assignment

## Welcome, Candidate!
Welcome to the PayEm Home Assignment! We're thrilled to have you here. This assignment is designed to give you a glimpse into the type of work you'll be tackling daily in this role, while also providing an opportunity for you to showcase your thought process and skill set. Rest assured, your solution will be used solely for evaluation purposes. We hope you find this experience both challenging and rewarding.

**Note:** For the backend portion of this assignment, please choose to implement either **Node.js** or **Python**, based on your preference.

---

## The Task
### **Frontend Requirements**
1. **Fetch and display a list of movies** with the following details:
   - Movie **name**
   - Movie **thumbnail** (image)
   - Movie **rating**
   - **Genre**
   - **Indicator if the user has watched the movie**
   - **Link to IMDb** page (opens in a new tab)
2. Movies should be displayed in a **grid layout**.
3. Users should be able to **mark a movie as watched**, and the UI should reflect this status.
4. Use **React with TypeScript** (no external state management required).
5. The UI should follow the **provided Figma design**.

### **Backend Requirements**
- Implement the backend in either **Python (Flask)** or **Node.js (Express)**.
- Use `db.json` as a local database (read/write operations required).
- Provide API endpoints for:
  1. **GET** `/api/movies` → Fetch all movies.
  2. **POST** `/api/movies` → Add a new movie. (**To be implemented**)
  3. **PUT** `/api/movies/:id` → Update an existing movie. (**To be implemented**)
- Use `fs` module (Node.js) or `json` module (Python) for reading/writing `db.json`.

---

## 🚀 Getting Started
### **Frontend Setup**
```sh
cd frontend
npm install
npm start
```

### **Backend Setup (Choose One)**
#### **Python (Flask)**
```sh
cd backend/python
pip install flask
python app.py
```
#### **Node.js (Express)**
```sh
cd backend/node
npm install
node server.js
```

🚀 **Good luck!**
