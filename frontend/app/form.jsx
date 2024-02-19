"use client"
export default function Form() {
  async function handler(e) {
    e.preventDefault();
    const form = e.target;
    const Data = new FormData(form);
    console.log(Data);
    // const res = await fetch('http://localhost:{ServerPort}/make-users', { method: "POST", body: JSON.stringify(Data) });
    // const product = res.json(); // Json with field config containing finished unique config for user 
    // TODO: output config
  }
  return (
    // TODO: Add checkbox for reverse proxy
    <form className="flex gap-5 flex-col align-center" method="POST" onSubmit={handler}>
      <input className="text-black w-1/4 justify-self-center" type="text" placeholder="Input e-mail" name="mail" />
      <input className="w-1/4 text-black" type="text" placeholder="Input name" name="login" />
      <button type="submit">Submit</button>
    </form >
  )
}
