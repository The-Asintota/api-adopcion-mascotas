import React from "react";
/* import firebase from 'frontend/utils/firebaseConfig.js' */
import { getStorage, ref, uploadBytes, getDownloadURL } from "firebase/storage";

const UploadLogo = () => {
  /* const [uploadingLogo, setUploadingLogo] = useState(false)*/
  const content = (
    <div>
      <span className="mb-2 block">
        Arrastra tus archivos aquí{" "}
      </span>
      <span className="mb-2 block">O</span>
      <span className="inline-flex rounded border border-[#e0e0e0] py-2 px-7 cursor-pointer">
        selecciónalos desde tu dispositivo
      </span>
    </div>
  );

  /*   const uploadedLogo = (
    <img src={} alt="uploaded" className= "max-w-56" />
  ); */

  return (
    <div className="mb-6 pt-4">
      <label className="mb-5 block text-white">
        Upload File
      </label>
      <div className="mb-8">
        <input
          type="file"
          /* onChange={handlePhotoChange} */
          name="photo"
          id="photo"
          className="sr-only"
          accept="image/*"
        />
        <label
          htmlFor="photo"
          className="relative flex min-h-[200px] items-center justify-center rounded-md border border-dashed border-[#e0e0e0] p-12 text-center"
        >
          {content}
        </label>
      </div>
    </div>
  );
};

export default UploadLogo;
