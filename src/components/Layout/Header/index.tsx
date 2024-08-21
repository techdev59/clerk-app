"use client";
import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
import Drawer from "@mui/material/Drawer";
import IconButton from "@mui/material/IconButton";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import { IoMenu } from "react-icons/io5";
import Toolbar from "@mui/material/Toolbar";
import Link from "next/link";
import { UserButton, useClerk, useUser } from "@clerk/nextjs";
import { MdPaid, MdSpaceDashboard } from "react-icons/md";
import { CgProfile } from "react-icons/cg";
import { RiTeamFill } from "react-icons/ri";
import { CiLogout } from "react-icons/ci";
import { useRouter } from "next/navigation";

export const drawerWidth = 240;

interface Props {
  /**
   * Injected by the documentation to work in an iframe.
   * Remove this when copying and pasting into your project.
   */
  window?: () => Window;
}

const NavLinksData = [
  { label: "Dashboard", path: "/dashboard", icon: <MdSpaceDashboard /> },
  { label: "Account", path: "/profile", icon: <CgProfile /> },
  { label: "Team", path: "/organization", icon: <RiTeamFill /> },
  { label: "Subscribe", path: "/subscribe", icon: <MdPaid /> },
];

export default function Header(props: Props) {
  const { window } = props;
  const { user, isLoaded } = useUser();
  const { signOut } = useClerk();
  const router = useRouter();
  const [mobileOpen, setMobileOpen] = React.useState(false);
  const [isClosing, setIsClosing] = React.useState(false);

  const handleDrawerClose = () => {
    setIsClosing(true);
    setMobileOpen(false);
  };

  const handleDrawerTransitionEnd = () => {
    setIsClosing(false);
  };

  const handleDrawerToggle = () => {
    if (!isClosing) {
      setMobileOpen(!mobileOpen);
    }
  };

  const drawer = (
    <div className="bg-blue-700 h-full">
      <List>
        <ListItem disablePadding className="text-white py-2">
          <ListItemButton>
            <UserButton afterSignOutUrl="/" />
            <div className="flex flex-col pl-4">
              <p>{user?.fullName}</p>
            </div>
          </ListItemButton>
        </ListItem>
        {NavLinksData.map((link, i) => (
          <ListItem key={i} disablePadding className="text-white w-full">
            <Link className="w-full" href={link.path}>
              <ListItemButton className="w-full">
                <ListItemIcon className="[&_svg]:text-white [&_svg]:w-6 [&_svg]:h-6">
                  {link.icon}
                </ListItemIcon>
                <ListItemText primary={link.label} />
              </ListItemButton>
            </Link>
          </ListItem>
        ))}
        <ListItem disablePadding className="text-white">
          <ListItemButton
            onClick={() => signOut(() => router.push("/sign-in"))}
          >
            <ListItemIcon className="[&_svg]:text-white [&_svg]:w-6 [&_svg]:h-6">
              <CiLogout />
            </ListItemIcon>
            <ListItemText primary="Logout" />
          </ListItemButton>
        </ListItem>
      </List>
    </div>
  );

  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <AppBar
        className="!bg-blue-700 md:!hidden"
        position="static"
        sx={{
          width: { sm: `calc(100% - ${drawerWidth}px)` },
          ml: { sm: `${drawerWidth}px` },
        }}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ mr: 2, display: { sm: "none" } }}
          >
            <IoMenu />
          </IconButton>
        </Toolbar>
      </AppBar>
      <Box
        component="nav"
        sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
        aria-label="mailbox folders"
      >
        <Drawer
          variant="temporary"
          open={mobileOpen}
          onTransitionEnd={handleDrawerTransitionEnd}
          onClose={handleDrawerClose}
          ModalProps={{
            keepMounted: true,
          }}
          sx={{
            display: { xs: "block", sm: "none" },
            "& .MuiDrawer-paper": {
              boxSizing: "border-box",
              width: drawerWidth,
            },
          }}
        >
          {drawer}
        </Drawer>
        <Drawer
          variant="permanent"
          sx={{
            display: { xs: "none", sm: "block" },
            "& .MuiDrawer-paper": {
              boxSizing: "border-box",
              width: drawerWidth,
            },
          }}
          open
        >
          {drawer}
        </Drawer>
      </Box>
    </Box>
  );
}
