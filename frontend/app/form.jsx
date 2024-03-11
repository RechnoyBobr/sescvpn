"use client"
import { useState, useEffect } from 'react'
export default function Form() {
  const [data, setData] = useState('');
  async function handler(e) {
    e.preventDefault();
    const form = e.target;
    const Data = { "email": form.email.value, "login": form.login.value };
    console.log(Data);
    const res = await fetch(`http://${process.env.BACKEND_HOST}:5000/create`, { method: "POST", body: JSON.stringify(Data) })
      .then(res => res.text())
      .then(res => setData(res));
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
