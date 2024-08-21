"use client";
import { ChildrenProps } from "@/types";
import { useUser } from "@clerk/nextjs";
import React from "react";
import Header from "../Header";
import { usePathname } from "next/navigation";

// UI Imports
import { ThemeProvider } from "@mui/material/styles";
import { theme } from "@/app/theme";
import { QueryClientProvider } from "@tanstack/react-query";
import { queryClient } from "@/utils/CommonFunctions";
import { Toaster } from "react-hot-toast";

const AuthRoutes = ["/sign-in", "/sign-up"];

const AppWrapper = ({ children }: ChildrenProps) => {
  const { user } = useUser();
  const pathName = usePathname();
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <main className="min-h-svh p-6 h-svh overflow-y-scroll">
          {user && <Header />}
          <div
            className={`h-full w-full ${
              AuthRoutes.includes(pathName)
                ? ""
                : `md:ml-[240px] md:w-[calc(100%-240px)]`
            }`}
          >
            {children}
          </div>
        </main>
        <Toaster
          position="top-center"
          reverseOrder={false}
          toastOptions={{
            className: "!bg-slate-700 !text-white",
          }}
        />
      </ThemeProvider>
    </QueryClientProvider>
  );
};

export default AppWrapper;
