import React, { useState } from "react";
import firebase from '/utils/firebaseConfig.js'
import { getStorage, ref, uploadBytes, getDownloadURL } from "firebase/storage";

const UploadLogo = ({onImageUpload}) => {
  const [uploadingLogo, setUploadingLogo] = useState(false)
  const [logoURL, setLogoURL] = useState(null)

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

  const uploadedLogo = (
    <img src={logoURL} alt="uploaded" className= "max-w-56" />
  )

  const waitingUpload = (
    <p>Uploading...</p>
  )

  const handleImageSelected = async (event) => {
    const selectedImage = event.target.files[0]

    if (!selectedImage) return;

    if (!selectedImage.type.startsWith("image/")) {
      console.log("El archivo no es una imagen")
      return;
    } /* puedo agregar que se muestre <ErrorMessage/> */

    setUploadingLogo(true)
    const storage = getStorage(firebase)
    const storageRef = ref(storage, "/sheltersLogos" + selectedImage.name )

    try {
      await uploadBytes(storageRef, selectedImage)
      const url = await getDownloadURL(storageRef)
      setLogoURL(url)
      onImageUpload(url)
    } catch (error){
      console.log(error)
    } finally {
      setUploadingLogo(false)
    }
  }

  return (
    <div className="mb-6 pt-4">
      <label className="mb-5 block text-white">
        Upload File
      </label>
      <div className="mb-8">
        <input
          type="file"
          onChange={handleImageSelected}
          name="photo"
          id="photo"
          className="sr-only"
          accept="image/*"
        />
        <label
          htmlFor="photo"
          className="relative flex min-h-[200px] items-center justify-center rounded-md border border-dashed border-[#e0e0e0] p-12 text-center"
        >
          {uploadingLogo ? waitingUpload : logoURL ? uploadedLogo : content}
        </label>
      </div>
    </div>
  );
};

export default UploadLogo;
