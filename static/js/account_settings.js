/**
 * Account Settings JavaScript
 * File: static/js/account_settings.js
 */

(function() {
    'use strict';
    
    console.log('✅ Account Settings JS loaded');

    // Delete image function
    function deleteImage(type) {
        console.log('🔴 Delete clicked:', type);
        
        const confirmMsg = type === 'profile' 
            ? 'Are you sure you want to delete your profile picture?' 
            : 'Are you sure you want to delete your banner image?';
        
        if (!confirm(confirmMsg)) {
            console.log('⚠️ User cancelled');
            return;
        }
        
        const hiddenFieldId = type === 'profile' ? 'delete_profile_picture' : 'delete_banner_image';
        const hiddenField = document.getElementById(hiddenFieldId);
        
        if (!hiddenField) {
            console.error('❌ Hidden field not found:', hiddenFieldId);
            alert('Error: Could not process deletion');
            return;
        }
        
        hiddenField.value = 'true';
        console.log('✅ Hidden field set to true:', hiddenFieldId);
        
        const form = document.getElementById('profileForm');
        if (!form) {
            console.error('❌ Form not found');
            alert('Error: Form not found');
            return;
        }
        
        console.log('📤 Submitting form...');
        form.submit();
    }

    // Attach event listeners when DOM is ready
    function attachDeleteListeners() {
        console.log('🔧 Attaching delete listeners');
        
        const deleteProfileBtn = document.getElementById('deleteProfileBtn');
        const deleteBannerBtn = document.getElementById('deleteBannerBtn');
        
        if (deleteProfileBtn) {
            console.log('✅ Found profile delete button');
            // Remove any existing listeners by cloning the button
            const newProfileBtn = deleteProfileBtn.cloneNode(true);
            deleteProfileBtn.parentNode.replaceChild(newProfileBtn, deleteProfileBtn);
            
            newProfileBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('🖱️ Profile delete button clicked');
                deleteImage('profile');
            });
        } else {
            console.log('ℹ️ No profile picture to delete');
        }
        
        if (deleteBannerBtn) {
            console.log('✅ Found banner delete button');
            // Remove any existing listeners by cloning the button
            const newBannerBtn = deleteBannerBtn.cloneNode(true);
            deleteBannerBtn.parentNode.replaceChild(newBannerBtn, deleteBannerBtn);
            
            newBannerBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('🖱️ Banner delete button clicked');
                deleteImage('banner');
            });
        } else {
            console.log('ℹ️ No banner image to delete');
        }
        
        console.log('✅ Listeners attached successfully');
    }

    // File validation
    function attachFileValidation() {
        console.log('🔧 Attaching file validation');
        
        const profileInput = document.getElementById('profile_picture');
        const bannerInput = document.getElementById('banner_image');
        
        if (profileInput) {
            profileInput.addEventListener('change', function() {
                const file = this.files[0];
                if (file) {
                    if (file.size > 2 * 1024 * 1024) {
                        alert('Profile picture must be less than 2MB');
                        this.value = '';
                        return;
                    }
                    const allowed = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif'];
                    if (!allowed.includes(file.type)) {
                        alert('Invalid file type. Use JPG, PNG, or GIF');
                        this.value = '';
                    }
                }
            });
        }
        
        if (bannerInput) {
            bannerInput.addEventListener('change', function() {
                const file = this.files[0];
                if (file) {
                    if (file.size > 2 * 1024 * 1024) {
                        alert('Banner image must be less than 2MB');
                        this.value = '';
                        return;
                    }
                    const allowed = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif'];
                    if (!allowed.includes(file.type)) {
                        alert('Invalid file type. Use JPG, PNG, or GIF');
                        this.value = '';
                    }
                }
            });
        }
    }

    // Initialize footer year
    function initFooter() {
        const displayYear = document.getElementById('displayYear');
        if (displayYear) {
            displayYear.textContent = new Date().getFullYear();
        }
    }

    // Main initialization function - RUNS ONLY ONCE
    function initAccountSettings() {
        console.log('🚀 Initializing account settings...');
        
        attachDeleteListeners();
        attachFileValidation();
        initFooter();
        
        console.log('✅ Account settings initialized');
    }

    // Initialize ONLY when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAccountSettings);
    } else {
        // DOM already loaded
        initAccountSettings();
    }

    console.log('✅ Account settings script fully loaded');
    
})();