
export default function Header() {
  return (
    <header>
      <div className="text-xl justify-between  m-5 flex gap-x-2.5 flex-row">
        <div className="flex flex-row gap-x-3.5 justify-evenly w-1/2">
          <div className="hover:text-sky-500 ease-in-out duration-300">Main</div>
          <div className="hover:text-sky-500 ease-in-out duration-300">Ne main</div>
        </div>
        <div className=" flex flex-row gap-x-3.5 justify-evenly w-1/2">
          <div><button className="hover:text-sky-500 ease-in-out duration-300">Reg</button></div>
          <div><button className="hover:text-sky-500 ease-in-out duration-300">Log in</button></div>
        </div>
      </div>
    </header>
  )
}
