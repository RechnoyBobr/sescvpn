export default function Form() {
  return (
    <form action="/make-user" className="flex gap-5 flex-col align-center" method="POST">
      <input className="text-black w-1/4 justify-self-center" type="text" placeholder="Input e-mail" name="mail" />
      <input className="w-1/4 text-black" type="text" placeholder="Input name" name="login" />
      <button type="submit">bebra</button>
    </form>
  )

}
