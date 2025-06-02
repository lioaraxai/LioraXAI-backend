// Enhanced LioraXAI Main JavaScript with Performance Optimizations
(function() {
    'use strict';
    
    // Performance monitoring
    const performanceMetrics = {
        startTime: performance.now(),
        loadTime: null,
        interactionTime: null
    };
    
    // Utility functions
    const utils = {
        // Debounce function for performance
        debounce: function(func, wait, immediate) {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    timeout = null;
                    if (!immediate) func(...args);
                };
                const callNow = immediate && !timeout;
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
                if (callNow) func(...args);
            };
        },
        
        // Throttle function for scroll events
        throttle: function(func, limit) {
            let inThrottle;
            return function() {
                const args = arguments;
                const context = this;
                if (!inThrottle) {
                    func.apply(context, args);
                    inThrottle = true;
                    setTimeout(() => inThrottle = false, limit);
                }
            };
        },
        
        // Check if element is in viewport
        isInViewport: function(element) {
            const rect = element.getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        },
        
        // Announce to screen readers
        announceToScreenReader: function(message) {
            const announcement = document.createElement('div');
            announcement.setAttribute('aria-live', 'polite');
            announcement.setAttribute('aria-atomic', 'true');
            announcement.className = 'sr-only';
            announcement.textContent = message;
            document.body.appendChild(announcement);
            setTimeout(() => {
                if (document.body.contains(announcement)) {
                    document.body.removeChild(announcement);
                }
            }, 1000);
        }
    };
    
    // Enhanced Dark Mode Management
    const darkModeManager = {
        init: function() {
            this.toggle = document.getElementById('darkModeToggle');
            this.prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
            this.savedMode = localStorage.getItem('lioraxai-dark-mode');
            
            this.setupInitialMode();
            this.bindEvents();
        },
        
        setupInitialMode: function() {
            const shouldUseDark = this.savedMode === 'dark' || 
                                 (!this.savedMode && this.prefersDarkScheme.matches);
            
            if (shouldUseDark) {
                this.enableDarkMode();
            } else {
                this.enableLightMode();
            }
        },
        
        enableDarkMode: function() {
            document.body.classList.add('dark-mode');
            if (this.toggle) {
                this.toggle.innerHTML = '<i class="bi bi-sun" aria-hidden="true"></i>';
                this.toggle.setAttribute('aria-label', 'Switch to light mode');
                this.toggle.setAttribute('title', 'Switch to light mode');
            }
        },
        
        enableLightMode: function() {
            document.body.classList.remove('dark-mode');
            if (this.toggle) {
                this.toggle.innerHTML = '<i class="bi bi-moon-fill" aria-hidden="true"></i>';
                this.toggle.setAttribute('aria-label', 'Switch to dark mode');
                this.toggle.setAttribute('title', 'Switch to dark mode');
            }
        },
        
        toggleMode: function() {
            const isDarkMode = document.body.classList.contains('dark-mode');
            
            if (isDarkMode) {
                this.enableLightMode();
                localStorage.setItem('lioraxai-dark-mode', 'light');
                utils.announceToScreenReader('Light mode enabled');
            } else {
                this.enableDarkMode();
                localStorage.setItem('lioraxai-dark-mode', 'dark');
                utils.announceToScreenReader('Dark mode enabled');
            }
        },
        
        bindEvents: function() {
            if (this.toggle) {
                this.toggle.addEventListener('click', () => this.toggleMode());
            }
            
            // Listen for system preference changes
            this.prefersDarkScheme.addEventListener('change', (e) => {
                if (!localStorage.getItem('lioraxai-dark-mode')) {
                    if (e.matches) {
                        this.enableDarkMode();
                    } else {
                        this.enableLightMode();
                    }
                }
            });
        }
    };
    
    // Enhanced Image Lazy Loading
    const lazyLoadManager = {
        init: function() {
            if ('IntersectionObserver' in window) {
                this.setupIntersectionObserver();
            } else {
                this.fallbackLazyLoad();
            }
        },
        
        setupIntersectionObserver: function() {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        this.loadImage(img);
                        observer.unobserve(img);
                    }
                });
            }, {
                rootMargin: '50px 0px',
                threshold: 0.01
            });
            
            document.querySelectorAll('img[data-src]').forEach(img => {
                img.classList.add('loading-skeleton');
                imageObserver.observe(img);
            });
        },
        
        loadImage: function(img) {
            img.src = img.dataset.src;
            img.classList.remove('loading-skeleton');
            img.addEventListener('load', () => {
                img.classList.add('loaded');
            });
            img.addEventListener('error', () => {
                img.classList.add('error');
                console.warn('Failed to load image:', img.dataset.src);
            });
        },
        
        fallbackLazyLoad: function() {
            // Fallback for browsers without IntersectionObserver
            document.querySelectorAll('img[data-src]').forEach(img => {
                this.loadImage(img);
            });
        }
    };
    
    // Enhanced Animation Manager
    const animationManager = {
        init: function() {
            this.prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
            this.setupAOS();
            this.bindEvents();
        },
        
        setupAOS: function() {
            if (typeof AOS !== 'undefined') {
                AOS.init({
                    duration: this.prefersReducedMotion.matches ? 0 : 600,
                    easing: 'ease-out-cubic',
                    once: true,
                    offset: 50,
                    disable: function() {
                        return window.innerWidth < 768 || 
                               window.matchMedia('(prefers-reduced-motion: reduce)').matches;
                    }
                });
            }
        },
        
        bindEvents: function() {
            this.prefersReducedMotion.addEventListener('change', () => {
                if (typeof AOS !== 'undefined') {
                    AOS.refresh();
                }
            });
        }
    };
    
    // Enhanced Scroll Manager
    const scrollManager = {
        init: function() {
            this.navbar = document.querySelector('.navbar');
            this.lastScrollTop = 0;
            this.bindEvents();
        },
        
        handleScroll: utils.throttle(function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            // Navbar scroll effect
            if (scrollManager.navbar) {
                if (scrollTop > 100) {
                    scrollManager.navbar.classList.add('navbar-scrolled');
                } else {
                    scrollManager.navbar.classList.remove('navbar-scrolled');
                }
            }
            
            scrollManager.lastScrollTop = scrollTop;
        }, 16), // ~60fps
        
        bindEvents: function() {
            window.addEventListener('scroll', this.handleScroll, { passive: true });
            
            // Smooth scroll for anchor links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
        }
    };
    
    // Performance Monitor
    const performanceMonitor = {
        init: function() {
            this.measureLoadTime();
            this.setupErrorHandling();
        },
        
        measureLoadTime: function() {
            window.addEventListener('load', () => {
                performanceMetrics.loadTime = performance.now() - performanceMetrics.startTime;
                console.log(`Page load time: ${performanceMetrics.loadTime.toFixed(2)}ms`);
            });
        },
        
        setupErrorHandling: function() {
            window.addEventListener('error', (e) => {
                console.error('JavaScript error:', e.error);
                // You could send this to an analytics service
            });
            
            window.addEventListener('unhandledrejection', (e) => {
                console.error('Unhandled promise rejection:', e.reason);
                // You could send this to an analytics service
            });
        }
    };
    
    // Enhanced Form Manager
    const formManager = {
        init: function() {
            this.setupFormValidation();
            this.setupFormSubmission();
        },
        
        setupFormValidation: function() {
            const forms = document.querySelectorAll('form');
            forms.forEach(form => {
                form.addEventListener('submit', this.handleFormSubmit.bind(this));
                
                // Real-time validation
                const inputs = form.querySelectorAll('input, textarea, select');
                inputs.forEach(input => {
                    input.addEventListener('blur', this.validateField.bind(this));
                    input.addEventListener('input', utils.debounce(this.validateField.bind(this), 300));
                });
            });
        },
        
        validateField: function(e) {
            const field = e.target;
            const isValid = field.checkValidity();
            
            field.classList.toggle('is-valid', isValid);
            field.classList.toggle('is-invalid', !isValid);
            
            // Update ARIA attributes
            field.setAttribute('aria-invalid', !isValid);
        },
        
        handleFormSubmit: function(e) {
            const form = e.target;
            const isValid = form.checkValidity();
            
            if (!isValid) {
                e.preventDefault();
                e.stopPropagation();
                
                // Focus first invalid field
                const firstInvalid = form.querySelector(':invalid');
                if (firstInvalid) {
                    firstInvalid.focus();
                }
            }
            
            form.classList.add('was-validated');
        },
        
        setupFormSubmission: function() {
            // Add loading states to form buttons
            document.querySelectorAll('form').forEach(form => {
                form.addEventListener('submit', function() {
                    const submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
                    if (submitBtn && form.checkValidity()) {
                        submitBtn.disabled = true;
                        submitBtn.innerHTML = '<i class="bi bi-hourglass-split me-2"></i>Sending...';
                    }
                });
            });
        }
    };
    
    // Resource Preloader
    const resourcePreloader = {
        init: function() {
            this.preloadCriticalResources();
            this.preloadNextPageResources();
        },
        
        preloadCriticalResources: function() {
            const criticalResources = [
                { href: '/static/images/logo.svg', as: 'image' },
                // Add more critical resources here
            ];
            
            criticalResources.forEach(resource => {
                const link = document.createElement('link');
                link.rel = 'preload';
                link.as = resource.as;
                link.href = resource.href;
                document.head.appendChild(link);
            });
        },
        
        preloadNextPageResources: function() {
            // Preload likely next pages on hover
            document.querySelectorAll('a[href^="/"]').forEach(link => {
                link.addEventListener('mouseenter', function() {
                    const href = this.getAttribute('href');
                    if (href && !document.querySelector(`link[rel="prefetch"][href="${href}"]`)) {
                        const prefetchLink = document.createElement('link');
                        prefetchLink.rel = 'prefetch';
                        prefetchLink.href = href;
                        document.head.appendChild(prefetchLink);
                    }
                }, { once: true });
            });
        }
    };
    
    // Main initialization
    document.addEventListener('DOMContentLoaded', function() {
        try {
            // Initialize all managers
            darkModeManager.init();
            lazyLoadManager.init();
            animationManager.init();
            scrollManager.init();
            formManager.init();
            resourcePreloader.init();
            performanceMonitor.init();
            
            // Set current year in footer
            const yearElement = document.getElementById('current-year');
            if (yearElement) {
                yearElement.textContent = new Date().getFullYear();
            }
            
            // Mark initialization complete
            performanceMetrics.interactionTime = performance.now() - performanceMetrics.startTime;
            console.log(`Interactive in: ${performanceMetrics.interactionTime.toFixed(2)}ms`);
            
        } catch (error) {
            console.error('Error during initialization:', error);
        }
    });
    
    // Export for potential external use
    window.LioraXAI = {
        utils,
        darkModeManager,
        performanceMetrics
    };
    
})(); 