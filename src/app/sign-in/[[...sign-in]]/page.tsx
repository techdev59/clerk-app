import { SignIn } from "@clerk/nextjs";

const SignInPage = () => {
  return (
    <div className="h-full flex items-center justify-center">
      <SignIn />
    </div>
  );
};
export default SignInPage;
