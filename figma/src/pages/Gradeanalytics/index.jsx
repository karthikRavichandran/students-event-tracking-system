import React from "react";

import { Sidebar } from "react-pro-sidebar";

import { Img, Text } from "../../components";

const GradeanalyticsPage = () => {
  return (
    <>
      <div className="bg-white-A700 flex font-fredokaone mx-auto relative w-full">
        <div className="flex flex-col mt-auto md:px-5 w-1/4">
          <div className="bg-white-A700 border-gray-300 border-r-[5px] border-solid h-20 mx-auto shadow-bs1 w-full"></div>
          <Sidebar className="!sticky !w-[314px] bg-white-A700 flex h-screen inset-[0] justify-center mb-auto mr-0.5 mt-[-80px] mx-auto overflow-auto pl-[30px] pr-[35px] py-[35px] shadow-bs2 top-[0] z-[1]"></Sidebar>
        </div>
        <div className="bg-white-A700 flex flex-col items-start justify-start ml-[-316px] mr-auto pt-[5px] px-[5px] shadow-bs3 w-full z-[1]">
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
        <div className="flex flex-col font-hammersmithone md:gap-10 gap-[98px] justify-start ml-[undefinedpx] mr-[115px] mt-[125px] md:px-5 w-[63%] z-[1]">
          <Text className="md:ml-[0] ml-[27px] sm:text-[21px] md:text-[23px] text-[25px] text-black-900">
            Grade Analytics
          </Text>
          <Img className="h-[360px] sm:h-auto object-cover w-full" src="images/img_image3.png" alt="imageThree" />
        </div>
      </div>
    </>
  );
};

export default GradeanalyticsPage;
