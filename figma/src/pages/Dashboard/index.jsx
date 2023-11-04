import React from "react";

import { Menu, MenuItem, Sidebar, useProSidebar } from "react-pro-sidebar";

import { Button, Img, Text } from "../../components";

const DashboardPage = () => {
  const { collapseSidebar, collapsed } = useProSidebar();

  return (
    <>
      <div className="bg-white-A700 flex mx-auto relative w-full">
        <div className="font-fredokaone h-[871px] mt-auto md:px-5 w-1/4">
          <div className="absolute flex flex-col inset-x-[0] items-center justify-start mx-auto top-[0] w-full">
            <div className="flex flex-col md:gap-10 gap-[412px] items-center justify-start w-full">
              <div className="bg-white-A700 border border-gray-300 border-solid h-20 shadow-bs1 w-full"></div>
              <div className="bg-blue_gray-100 h-[81px] w-full"></div>
            </div>
          </div>
          <Sidebar
            onClick={() => collapseSidebar(!collapsed)}
            className="!sticky !w-[314px] bg-white-A700 flex h-screen md:hidden inset-[0] justify-center m-auto overflow-auto shadow-bs2 top-[0]"
          >
            <Menu
              menuItemStyles={{
                button: {
                  padding: " ",
                  paddingLeft: "30px",
                  gap: "33px",
                  margin: " ",
                  color: "#000000",
                  fontSize: "24px",
                },
              }}
              className="flex flex-col items-center justify-start mb-[287px] mt-32 md:pr-10 sm:pr-5 pr-[116px] w-[64%]"
            >
              <MenuItem
                icon={<Img className="h-9" src="images/img_grid.svg" alt="grid" />}
                active={window.location.pathname === "/"}
                href="/"
              >
                <Text className="md:text-[22px] sm:text-xl">Dashboard</Text>
              </MenuItem>
              <Img className="h-[49px] mt-[371px]" src="images/img_info.svg" alt="info" />
            </Menu>
          </Sidebar>
        </div>
        <div className="bg-white-A700 flex flex-col font-fredokaone items-start justify-start ml-[-316px] mr-auto pt-[5px] px-[5px] shadow-bs3 w-full z-[1]">
          <div className="flex flex-col items-center justify-start mt-0.5 md:px-5 w-[95%] md:w-full">
            <div className="flex md:flex-col flex-row md:gap-5 items-center justify-end w-full">
              <div className="flex md:flex-1 flex-col gap-1.5 items-center justify-start w-[26%] md:w-full">
                <Img className="h-[35px] w-[35px]" src="images/img_user.svg" alt="user" />
                <Text className="sm:text-[21px] md:text-[23px] text-[25px] text-light_blue-700_01">
                  STUDENT EVENT TRACK
                </Text>
              </div>
              <Img className="h-11 md:ml-[0] ml-[619px]" src="images/img_notification.svg" alt="notification" />
              <Text className="ml-4 md:ml-[0] sm:text-[21px] md:text-[23px] text-[25px] text-light_blue-700">
                User name
              </Text>
              <div className="bg-white-A700 flex md:flex-1 flex-col items-center justify-start mb-[3px] ml-1.5 md:ml-[0] md:mt-0 mt-3 p-2 w-[5%] md:w-full">
                <Img className="h-[39px]" src="images/img_user_gray_900.svg" alt="user_One" />
              </div>
              <Img className="h-6 md:ml-[0] ml-[7px] w-6" src="images/img_location.svg" alt="location" />
            </div>
          </div>
        </div>
        <div className="bg-light_blue-200 flex flex-row font-hammersmithone gap-[9px] items-center justify-start ml-[undefinedpx] mt-[272px] p-[18px] md:px-5 shadow-bs w-1/4 z-[1]">
          <Img className="h-[39px] ml-8 my-0.5" src="images/img_user_light_blue_700.svg" alt="user_Two" />
          <Text className="sm:text-[21px] md:text-[23px] text-[25px] text-black-900">User information</Text>
        </div>
        <Button
          className="cursor-pointer flex items-center justify-center left-[0] min-w-[315px] ml-[undefinedpx] mt-[356px] top-[0] z-[1]"
          leftIcon={
            <Img
              className="mr-[7px] right-[1%] ml-[undefinedpx] z-[1]"
              src="images/img_bxsnotification.svg"
              alt="bxs:notification"
            />
          }
        >
          <div className="font-hammersmithone md:text-[23px] sm:text-[21px] text-[25px] text-left z-[1]">Alerts</div>
        </Button>
        <Button
          className="bottom-[0] cursor-pointer flex items-center justify-center left-[0] mb-[310px] min-w-[316px] ml-[undefinedpx] z-[1]"
          leftIcon={
            <div className="mt-px mb-1 mr-3.5 bg-light_blue-700 right-[1%] ml-[undefinedpx] z-[1] inset-y-[0]">
              <Img className="ml-[undefinedpx] z-[1]" src="images/img_checkmark.svg" alt="checkmark" />
            </div>
          }
          size="sm"
        >
          <div className="font-hammersmithone md:text-[23px] sm:text-[21px] text-[25px] text-left z-[1]">
            Grade Analytics{" "}
          </div>
        </Button>
        <Button
          className="bottom-[0] cursor-pointer flex items-center justify-center left-[0] mb-[226px] min-w-[316px] ml-[undefinedpx] z-[1]"
          leftIcon={<Img className="mr-4 right-[1%] ml-[undefinedpx] z-[1]" src="images/img_info.svg" alt="info" />}
        >
          <div className="font-hammersmithone md:text-[23px] sm:text-[21px] text-[25px] text-left z-[1]">
            Course info
          </div>
        </Button>
        <div className="flex flex-col font-hammersmithone justify-start ml-[undefinedpx] mr-[74px] my-auto md:px-5 w-[66%] z-[1]">
          <Text className="sm:text-[21px] md:text-[23px] text-[25px] text-black-900"> Welcome back, User name! 👋</Text>
          <Text className="md:ml-[0] ml-[53px] mt-11 sm:text-[21px] md:text-[23px] text-[25px] text-black-900">
            Alerts
          </Text>
          <Img
            className="h-[458px] sm:h-auto md:ml-[0] ml-[27px] mt-3.5 object-cover w-[97%] md:w-full"
            src="images/img_image1.png"
            alt="imageOne"
          />
        </div>
      </div>
    </>
  );
};

export default DashboardPage;
