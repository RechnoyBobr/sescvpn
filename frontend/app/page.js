import Image from "next/image";
import Header from "./header";
import Form from "./form";
export default function Home() {
  return (
    <div className="my-7 container flex justify-center align-center flex-col px-5">
      <Header />
      <Form />
    </div>
  );
}
