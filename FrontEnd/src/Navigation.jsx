import React from 'react';
import { Link } from 'react-router-dom';
import { scroll } from '../App';

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/" onClick={() => scroll.animateScroll(document.getElementById('header'))}>Home</Link>
        </li>
        <li>
          <Link to="/features" onClick={() => scroll.animateScroll(document.getElementById('features'))}>Features</Link>
        </li>
        {/* ... other links ... */}
      </ul>
    </nav>
  );
};