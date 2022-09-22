// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCuPtF109OHpADcs9ZEf0z-WjJoryvTaP4",
  authDomain: "alpr-streamlit.firebaseapp.com",
  projectId: "alpr-streamlit",
  storageBucket: "alpr-streamlit.appspot.com",
  messagingSenderId: "1056701039619",
  appId: "1:1056701039619:web:acab057832f63c8fea7a36",
  measurementId: "G-SWWP8E35HB",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
