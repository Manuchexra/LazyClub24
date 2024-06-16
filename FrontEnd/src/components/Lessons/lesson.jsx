// src/components/Lesson.js
import React, { useState, useEffect } from 'react';
import authService from '../auth/authService.js'; // Import authService correctly
import './Lessons.css'; // Import the CSS file

const Lesson = () => {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const lessonData = await authService.fetchLessons(); // Use fetchLessons for calling the function
        setLessons(lessonData); 
        setLoading(false); 
      } catch (error) {
        console.error('Error fetching lesson data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="lesson-container">
      <h1>Lessons</h1>
      <ul>
        {lessons.map(lesson => (
          <li key={lesson.id}>
            <h2>{lesson.title}</h2>
            <img src={lesson.photo} alt={lesson.title} /> 
            <p>{lesson.information}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Lesson;
