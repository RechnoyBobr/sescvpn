"use client"
import { useState, useEffect } from 'react'
export default function Form() {
  const [data, setData] = useState('');
  async function handler(e) {
    e.preventDefault();
    const form = e.target;
    console.log(form.login.value)
    const Data = { "login": form.login.value, "email": form.email.value }
    const res = await fetch('http://localhost:5000/create', { method: "POST", body: JSON.stringify(Data) })
      .then(response => response.text())
      .then(response => setData(response))

    //const product = res.json(); // Json with field config containing finished unique config for user 
  }
  return (
    <div>
      <form className="flex gap-5 flex-col align-center" method="POST" onSubmit={handler}>
        <input className="text-black w-1/4 justify-self-center" type="text" placeholder="Input e-mail" name="email" />
        <input className="w-1/4 text-black" type="text" placeholder="Input name" name="login" />
        <button type="submit">Submit</button>
      </form >
      <div>{data}</div>
    </div>
  )
}
