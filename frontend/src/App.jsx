import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [courses, setCourses] = useState([])

  useEffect(() => {
    fetch(import.meta.env.VITE_API_URL)
      .then((r) => r.json())
      .then(setCourses)
      .catch((e) => console.error(e))
  }, [])

  return (
    <div className="App">
      <h1>Easy GE Finder</h1>
      <ul>
        {courses.map((c) => (
          <li key={`${c.subject}${c.catalog}`}>{c.subject} {c.catalog} – GPA {c.average_grade.toFixed(2)}</li>
        ))}
      </ul>
    </div>
  )
}

export default App
